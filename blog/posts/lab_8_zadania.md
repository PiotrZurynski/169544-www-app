Zapytania

Wszystkie kategorie
{
  allCategories {
    id
    name
    description
  }
}

Kategorie po  id

{
  categoryById(id: 2) {
    id
    name
    description
  }
}

Wszystkie topiki
{
  allTopics {
    id
    name
    created
    category {
      id
      name
    }
  }
}

Topik po id
{
  topicById(id: 1) {
    id
    name
    created
    category {
      id
      name
    }
  }
}


Wszystkie posty
{
  allPosts {
    id
    title
    slug
    topic {
      id
      name
    }
    createdBy {
      id
      username
    }
    createdAt
    updatedAt
  }
}

Post po id
{
  postById(id: 8) {
    id
    title
    text
    slug
    topic { id name }
    createdBy { id username }
    createdAt
    updatedAt
  }
}


Resolvery zapytania

filter do kategorii po fragmencie nazwy
{
  categoriesByName(nameFragment: "techno") {
    id
    name
    description
  }
}

filter do postow po fragmencie sluga
{
  postsBySlug(slugFragment: "test") {
    id
    title
    slug
    createdBy { username }
  }
}

liczba postow dla danego usera
{
  postsCountByUser(userId: 1)
}


zapytania mutations

create post
mutation {
  createPost(
    title: "testpost"
    text: "test"
    topicId: 1
    slug: "test"
    createdById: 1
  ) {
    post {
      id
      title
      text
      slug
      topic { id name }
      createdBy { id username }
      createdAt
    }
    success
    message
  }
}

update post

mutation {
  updatePost(
    id: 8
    title: "testpostpost"
    text: "test"
    slug: "test"
  ) {
    post {
      id
      title
      text
      slug
      updatedAt
    }
    success
    message
  }
}


delete post
mutation {
  deletePost(id: 8) {
    success
    message
  }
}

